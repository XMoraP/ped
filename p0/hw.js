try {
    greet = console.log	// node.js
} catch (e) {
    greet = print	// Rhino
}
greet('Hello World!')
