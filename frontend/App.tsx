import React, { useState, useCallback, useEffect } from 'react';
import { StatusBar, StyleSheet, Text, View } from 'react-native';
import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context';
import { GiftedChat, IMessage } from 'react-native-gifted-chat';
import { Colors } from './src/theme/colors';

const App = () => {
    const [messages, setMessages] = useState<IMessage[]>([]);

    useEffect(() => {
        setMessages([
            {
                _id: '1',
                text: '¡Bienvenido! Soy tu asistente. ¿En qué puedo ayudarte?',
                createdAt: new Date(),
                user: { _id: 2, name: 'Asistente' },
            },
        ]);
    }, []);

    const onSend = useCallback(async (newMessages: IMessage[] = []) => {
        setMessages((prev) => GiftedChat.append(prev, newMessages));
        const text = newMessages[0].text;

        try {
            const response = await fetch('http://localhost:8000/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text }),
            });
            const data = await response.json();

            const botMsg: IMessage = {
                _id: String(Math.random()),
                text: data.reply,
                createdAt: new Date(),
                user: { _id: 2, name: 'Asistente' },
            };
            setMessages((prev) => GiftedChat.append(prev, [botMsg]));
        } catch (e) {
            console.error("Error de conexión con FastAPI", e);
        }
    }, []);

    return (
        <SafeAreaProvider>
            <SafeAreaView style={styles.container} edges={['right', 'bottom', 'left']}>
                <StatusBar barStyle="light-content" backgroundColor={Colors.primary} />
                <View style={styles.header}>
                    <Text style={styles.title}>Asistente Davivienda</Text>
                </View>
                <View style={styles.chatContainer}>
                    <GiftedChat
                        messages={messages}
                        onSend={(msgs: IMessage[]) => onSend(msgs)}
                        user={{ _id: 1 }}
                        textInputProps={{
                            placeholder: "Escribe un mensaje...",
                            style: { color: '#000', flex: 1, paddingHorizontal: 10 }
                        }}
                    />
                </View>
            </SafeAreaView>
        </SafeAreaProvider>
    );
};

const styles = StyleSheet.create({
    container: { flex: 1, backgroundColor: Colors.background },
    header: { backgroundColor: Colors.primary, padding: 20, alignItems: 'center' },
    title: { color: '#ffffff', fontSize: 20, fontWeight: 'bold' },
    chatContainer: { flex: 1 },
});

export default App;