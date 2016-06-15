var CpuMemStats = function() {

    var instance = this;
    var cpubars = [];

    
    this.updateCpu = function(msg) {
	cpuStatus = eval(msg);
	console.log(cpuStatus);

	if (cpubars.length == 0)
	    instance.init(cpuStatus.length);


	cpubars.forEach(function(cpu, index) {
	    console.log("CPU " + index + ": " + cpuStatus[index] + "%");
	    $(cpu).css("height", cpuStatus[index] + "%");
	});

	
    }
    
    //constructor must be called init for the web frontend to initialize
    //when this plugin is loaded
    this.init = function(cpuCount) {
	for (var i = 0; i < cpuCount; i++) {

	    var container = document.createElement("div");
	    $(container).addClass("cpubar-container");
	    
	    var label = document.createElement("div");
	    $(label).addClass("cpubar-label").appendTo($(container)).text(i);
	    
	    var level = document.createElement("div");
	    $(level).addClass("cpubar-level").appendTo($(container));



	    
	    cpubars.push(level);
	    $("#SysInfo2").append(container);
	    
	}
    }
    
    //destructor must be named 'destroy' for web frontend to cleanup
    //when unloading this plugin
    this.destroy = function() {
	
    }

};
