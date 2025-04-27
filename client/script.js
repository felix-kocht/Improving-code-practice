const apiUrl = "http://localhost:8000/tasks";  // Adjust if your server is on a different port

document.getElementById("addTaskButton").addEventListener("click", addTask);

function addTask() {
    const name = document.getElementById("taskName").value;

    fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            name: name,
            date: null,
            completed: false
        })
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById("taskName").value = "";
        loadTasks();  // Reload the list
    });
}

function loadTasks() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(tasks => {
            const list = document.getElementById("taskList");
            list.innerHTML = "";  // Clear previous
            tasks.forEach(task => {
                const item = document.createElement("li");
                item.textContent = task.name + (task.completed ? " (completed)" : "");
                list.appendChild(item);
            });
        });
}

// Load tasks when page loads
window.onload = loadTasks;