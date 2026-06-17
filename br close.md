    window.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            // 1. Blocks the app's global scripts from seeing the Escape key
            event.stopImmediatePropagation();
            
            // 2. Prevents any default browser-level actions
            event.preventDefault();
            
            console.log("Logout prevented! Safe to switch tabs.");
        }
    }, true); // 'true' runs this first, before the app's logout script can trigger

lllll

    // Paste this JavaScript snippet into your automation script's execution block
    Object.defineProperty(document, 'visibilityState', { value: 'visible', writable: true });
    Object.defineProperty(document, 'hidden', { value: false, writable: true });
    
    // Block the website from knowing the window lost focus
    window.addEventListener('visibilitychange', function(e) {
        e.stopImmediatePropagation();
    }, true);
    
    window.addEventListener('blur', function(e) {
        e.stopImmediatePropagation();
    }, true);
