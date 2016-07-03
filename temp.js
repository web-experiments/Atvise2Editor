webMI.data.read("AGENT.OBJECTS.test1", function(f) {
	var value = f.value;
	webMI.gfx.setRotation(id, webMI.translate(value, false, false, 0, 180));
    console.log("Test");
});


