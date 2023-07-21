function appendMessage(user, message) {
    const chatBox = document.getElementById("chatBox");
    const messageDiv = document.createElement("div");
    messageDiv.innerHTML = `<p><strong>${user}:</strong> ${message}</p>`;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom of chat box
}

function sendMessage() {
    const userMessageInput = document.getElementById("userMessage");
    const userMessage = userMessageInput.value.trim();

    if (userMessage !== "") {
        // Assuming "Bot" responds in the server (not implemented in this client-side example)
        // Replace "Bot" with the actual name of the bot if needed
        appendMessage("User", userMessage);
        userMessageInput.value = "";
    }
}

// Sample code to receive chat data from the server and populate the chat box
// You can use this function if you're loading chat data dynamically from the server
function loadChatDataFromServer() {
    // Replace the URL with your server endpoint for getting chat data
    fetch('/botchat')
        .then(response => response.json())
        .then(data => {
            data.forEach(message => {
                appendMessage(message.user, message.message);
            });
        })
        .catch(error => console.error('Error loading chat data:', error));
}

// Uncomment the line below if you want to load chat data from the server on page load
// window.addEventListener('DOMContentLoaded', loadChatDataFromServer);