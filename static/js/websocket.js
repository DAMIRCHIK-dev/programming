  // static/js/websocket.js
(function(){
  const protocol = window.location.protocol === "https:" ? "wss" : "ws";
  const socket = new WebSocket(`${protocol}://${window.location.host}/ws/inventory/`);

  socket.onopen = () => console.log("WebSocket: connected");
  socket.onclose = () => console.log("WebSocket: disconnected");

  socket.onmessage = event => {
    const { type, message } = JSON.parse(event.data);
    if (type === "update") {
      // Misol: yangi delivery haqida pop-up bildirishnoma
      const info = `New delivery: ${message.ingredient} (${message.quantity}g) by ${message.user}`;
      // oddiy alert, keyinchalik Toast-ga o'zgartirishingiz mumkin
      alert(info);

      // Yangi delivery kartasini sahifaga inject qilish uchun AJAX/DOM manipulyatsiya yozing
      // masalan: document.getElementById("deliveries").prepend(…)
    }
  };
})();

// static/js/main.js
const mealLogSocket = new WebSocket(
  (location.protocol === "https:" ? "wss://" : "ws://") +
  window.location.host +
  "/ws/meal-log/"
);

mealLogSocket.onmessage = e => {
  const data = JSON.parse(e.data);
  console.log("Meal log:", data);
};
