s.waitForBoot({
	//(
	//basic synth
	SynthDef(\vemlTest,{
		arg lux = 1;
		var freq = 440, sig;

		sig = SinOsc.ar(440 + SinOsc.ar(lux * 20, mul:10));
		Out.ar(0, sig!2);
	}).add;


	//
	~hiLux = 0;
	~loLux = 100;
	// this funcion scales the lux values to be between 0 and 1
	~scaledLux = {|val|(val - ~loLux) / (~hiLux - ~loLux)};

	Task({
		1.wait;
		x = Synth(\vemlTest);
	}).play;

	OSCdef.freeAll;
	OSCdef(\testOSCFunc,
		{
			|msg, time, addr, recvPort|
			var inLux, lux;
			//[msg, time, addr, recvPort].postln;
			inLux = msg[1];
			/*checks if each incoming lux is higher or lower than the previous highest or lowest values.
			If the new value is higher, it sets a new high value. If it's lower, it sets a new low value*/
			if(inLux > ~hiLux, {~hiLux = inLux; ("Highest Lux: " ++ ~hiLux).postln});
			if(inLux < ~loLux, {~loLux = inLux; ("Lowest Lux: " ++ ~loLux).postln});

			lux = ~scaledLux.value(inLux);
			lux.postln;
			x.set(\lux, lux);

		},
		path: \veml7700,
		recvPort: 5005);

	//)
});
s.boot;

