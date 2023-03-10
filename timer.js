//678HaeS07xeoZEmdscDf 

var push = require( 'pushsafer-notifications' );
 
var p = new push( {
    k: '678HaeS07xeoZEmdscDf',             // your 20 chars long private key 
    debug: true
});
 
var msg = {
    m: 'Feed MiHi his food',   // message (required)
    t: "Lil Dragon timer",                     // title (optional)
    s: '8',                                // sound (value 0-50) 
    v: '2',                                // vibration (empty or value 1-3) 
    i: '5',                                // icon (value 1-176)
    c: '#FF0000',                          // iconcolor (optional)
    u: 'https://www.pushsafer.com',        // url (optional)
    ut: 'Open Link',                       // url title (optional)
    d: 'a'                               // the device or device group id 
};
 
// console.log( p ); 
 
p.send( msg, function( err, result ) {
    //console.log( 'ERROR:', err ); 
    console.log( 'RESULT', result );
    // process.exit(0); 
});