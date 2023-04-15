const package = require('./package.json');
const nodeVersion = process.version;

if (package.nodeVersion == nodeVersion) {
    console.log(`Everything is OK (${package.nodeVersion} == ${nodeVersion})`);
}else{
    console.log(`You are using a different version of nodejs (${package.nodeVersion} != ${nodeVersion})`);
}