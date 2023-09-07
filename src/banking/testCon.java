package banking;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class testCon {


    // Database URL, username, and password

    String url = "jdbc:mysql://localhost:3307/feedback";
    String dbuser = "sqluser";
    String dbpass = "sqluserpw";

    try {       
     
       // Register the MySQL JDBC driver
       Class.forName("com.mysql.cj.jdbc.Driver");
       
       Connection connection = DriverManager.getConnection(url, dbuser, dbpass);

    } catch (Exception e) {

        // TODO: handle exception
    
    }
   
}