s.waitForBoot({
	//
	~hiLux = 0;
	~loLux = 100;

	OSCdef.freeAll;
	OSCdef(\testOSCFunc,
		{
			|msg, time, addr, recvPort|;
			[msg, time, addr, recvPort].postln;

			if(msg[2] > ~hiLux, {~hiLux = msg[2]; ("Highest Lux: " ++ ~hiLux).postln});
			if(msg[2] < ~loLux, {~loLux = msg[2]; ("Lowest Lux: " ++ ~loLux).postln});

		},
		path: \test,
		recvPort: 5005);


});
s.boot;
