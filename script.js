document.getElementById('sendButton').addEventListener('click', async () => {
    const userInput = document.getElementById('userInput').value;

    try {
        const response = await fetch('/api/process', {  // Ruta relativa
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ input: userInput }),
        });

        const data = await response.json();
        console.log("Respuesta del servidor:", data); // Depuración
        document.getElementById('responseOutput').innerText = data.result;
    } catch (error) {
        console.error('Error al enviar la solicitud:', error);
    }
});
