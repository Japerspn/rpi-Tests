s.waitForBoot({
//(
	OSCdef.freeAll;
	OSCdef(\testOSCFunc,
		{
			|msg, time, addr, recvPort|
			[msg, time, addr, recvPort].postln;
		},
		path: \test,
		recvPort: 5005);

//)
});
s.boot;
