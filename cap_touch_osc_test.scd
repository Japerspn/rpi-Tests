s.waitForBoot({
//(
	OSCdef.freeAll;
	OSCdef(\testOSCFunc,
		{
			|msg, time, addr, recvPort| [msg, time, addr, recvPort].postln;

			if( msg[2] == 'touched', {
				msg.postln;
			});
			if( msg[2] == 'released', {
				msg.postln;
			});


		},
		path: \test,
		recvPort: 5005);

//)
});
s.boot;
