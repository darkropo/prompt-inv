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
        appendMessage("User", userMessage);
        userMessageInput.value = "";

        // Send the user's message to the API endpoint using AJAX
        fetch('/botchat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user: 'User',
                message: userMessage
            })
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the server if needed
            // For example, append the bot's response to the chat box
            appendMessage("Bot", data.bot_response);
        })
        .catch(error => console.error('Error sending message:', error));
    }
}

// Function to clear the chat box
function clearChat() {
    const chatBox = document.getElementById("chatBox");
    chatBox.innerHTML = ""; // Clear all chat messages
}
// Function to handle sending a message when Enter key is pressed
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

// Sample code to receive chat data from the server and populate the chat box
// You can use this function if you're loading chat data dynamically from the server
// function loadChatDataFromServer() {
//     // Replace the URL with your server endpoint for getting chat data
//     fetch('/botchat')
//         .then(response => response.json())
//         .then(data => {
//             data.forEach(message => {
//                 appendMessage(message.user, message.message);
//             });
//         })
//         .catch(error => console.error('Error loading chat data:', error));
// }

// Uncomment the line below if you want to load chat data from the server on page load
// window.addEventListener('DOMContentLoaded', loadChatDataFromServer);