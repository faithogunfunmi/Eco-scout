import App from "./App.jsx";

// Service worker remains inactive
// Potential advancements : Include notifications to let user know when the extension detects a brand in its database


chrome.runtime.onStartup.addListener( () => {
    console.log(`onStartup()`);
});