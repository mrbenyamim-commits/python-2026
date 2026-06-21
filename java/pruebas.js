import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, FlatList } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

export default function App() {
  const [items, setItems] = useState([]);
  const [text, setText] = useState('');

  // Cargar datos al iniciar
  useEffect(() => {
    cargarDatos();
  }, []);

  const guardarDatos = async (nuevosItems) => {
    try {
      await AsyncStorage.setItem('@mi_app_datos', JSON.stringify(nuevosItems));
      setItems(nuevosItems);
    } catch (e) {
      console.error("Error guardando datos", e);
    }
  };

  const cargarDatos = async () => {
    try {
      const valor = await AsyncStorage.getItem('@mi_app_datos');
      if (valor !== null) {
        setItems(JSON.parse(valor));
      }
    } catch (e) {
      console.error("Error cargando datos", e);
    }
  };

  const agregarItem = () => {
    if (text.trim() === '') return;
    const nuevosItems = [...items, { id: Date.now().toString(), nombre: text }];
    guardarDatos(nuevosItems);
    setText('');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Mi Proyecto Express</Text>
      
      <View style={styles.inputContainer}>
        <TextInput 
          style={styles.input} 
          placeholder="Escribe algo aquí..." 
          value={text}
          onChangeText={setText}
        />
        <TouchableOpacity style={styles.button} onPress={agregarItem}>
          <Text style={styles.buttonText}>Añadir</Text>
        </TouchableOpacity>
      </View>

      <FlatList 
        data={items}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.card}>
            <Text>{item.nombre}</Text>
          </View>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, paddingTop: 60, paddingHorizontal: 20, backgroundColor: '#f5f5f5' },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20, textAlign: 'center' },
  inputContainer: { flexDirection: 'row', marginBottom: 20 },
  input: { flex: 1, backgroundColor: '#fff', padding: 10, borderRadius: 5, marginRight: 10, borderComposite: 1, borderColor: '#ddd' },
  button: { backgroundColor: '#007AFF', padding: 12, borderRadius: 5, justifyContent: 'center' },
  buttonText: { color: '#fff', fontWeight: 'bold' },
  card: { backgroundColor: '#fff', padding: 15, borderRadius: 5, marginBottom: 10, elevation: 1 }
});