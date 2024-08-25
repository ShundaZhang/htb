document.addEventListener("DOMContentLoaded", () => {
    const tornadoList = document.getElementById("tornado-list");

    const getStatusClass = (status) => {
        if (status.toLowerCase() === "active") {
            return "status-active";
        } else if (status.toLowerCase() === "inactive") {
            return "status-inactive";
        } else {
            return "status-unknown";
        }
    };

    const createListItem = (tornado) => {
        const listItem = document.createElement("li");
        listItem.className = "list-group-item";
    
        const icon = document.createElement("i");
        icon.className = "las la-bolt icon";
    
        const text = document.createElement("span");
        text.className = "text";
    
        const machineIdLabel = document.createElement("span");
        machineIdLabel.className = "label";
        machineIdLabel.style.color = "white";
        machineIdLabel.innerHTML = "Machine ID: ";
    
        const machineIdValue = document.createElement("span");
        machineIdValue.className = "machine-id";
        machineIdValue.innerHTML = tornado.machine_id;
    
        const machineIdContainer = document.createElement("span");
        machineIdContainer.appendChild(machineIdLabel);
        machineIdContainer.appendChild(machineIdValue);
    
        const iconGlobe = document.createElement("i");
        iconGlobe.className = "las la-globe icon";
    
        const ipAddressLabel = document.createElement("span");
        ipAddressLabel.className = "label";
        ipAddressLabel.style.color = "white";
        ipAddressLabel.innerHTML = "IP: ";
    
        const ipAddressValue = document.createElement("span");
        ipAddressValue.className = "ip-address";
        ipAddressValue.innerHTML = tornado.ip_address;
    
        const ipAddressContainer = document.createElement("span");
        ipAddressContainer.appendChild(iconGlobe);
        ipAddressContainer.appendChild(ipAddressLabel);
        ipAddressContainer.appendChild(ipAddressValue);
    
        text.appendChild(machineIdContainer);
        text.appendChild(ipAddressContainer);
    
        const status = document.createElement("span");
        status.className = `status ${getStatusClass(tornado.status)}`;
        status.innerHTML = tornado.status;
    
        listItem.appendChild(icon);
        listItem.appendChild(text);
        listItem.appendChild(status);
    
        return listItem;
    };

    const fetchTornados = () => {
        tornadoList.innerHTML = "";
        fetch("/get_tornados")
            .then(response => response.json())
            .then(data => {
                data.forEach(tornado => {
                    if (!tornado.machine_id && !tornado.ip_address && !tornado.status) {
                        return;
                    }
                    const listItem = createListItem(tornado);
                    tornadoList.appendChild(listItem);
                });
            });
    };

    fetchTornados();

    document.getElementById("update-form").addEventListener("submit", (event) => {
        event.preventDefault();
        const machineId = document.getElementById("machine-id").value;
        const status = document.getElementById("status").value;

        fetch("/update_tornado", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ machine_id: machineId, status: status })
        })
            .then(response => response.json())
            .then(data => {
                const updateMessage = document.getElementById("update-message");
                if (data.error) {
                    updateMessage.textContent = `Error: ${data.error.message}`;
                    updateMessage.className = "text-danger";
                } else {
                    updateMessage.textContent = data.success.message;
                    updateMessage.className = "text-success";
                    fetchTornados();
                }
            })
            .catch(error => {
                const updateMessage = document.getElementById("update-message");
                updateMessage.textContent = `Error updating status: ${error.message}`;
                updateMessage.className = "text-danger";
            });
    });

    document.getElementById("report-form").addEventListener("submit", (event) => {
        event.preventDefault();
        const ipAddress = document.getElementById("ip-address").value;

        fetch(`/report_tornado?ip=${ipAddress}`)
            .then(response => response.json())
            .then(data => {
                const reportMessage = document.getElementById("report-message");
                if (data.error) {
                    reportMessage.textContent = `Error: ${data.error.message}`;
                    reportMessage.className = "text-danger";
                } else {
                    reportMessage.textContent = data.success.message;
                    reportMessage.className = "text-success";
                }
            })
            .catch(error => {
                const reportMessage = document.getElementById("report-message");
                reportMessage.textContent = `Error reporting tornado: ${error.message}`;
                reportMessage.className = "text-danger";
            });
    });
    
    window.addEventListener("message", (event) => {
        const tornado = event.data;

        if (!tornado.machine_id && !tornado.ip_address && !tornado.status) {
            return;
        }

        const listItem = createListItem(tornado);
        tornadoList.appendChild(listItem);
    });
});
