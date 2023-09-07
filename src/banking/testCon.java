package banking;

import java.sql.Connection;
import java.sql.DriverManager;

public class testCon {

    public void connectionTest() 
    
    {
        // Database URL, username, and password
        try {
            // Register the MySQL JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            // Establish a connection to the database
            Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3307/feedback?" + "user=root&password=password");

            if (connection != null) {
                System.out.println("Connected to the database!");
                // Perform database operations here
                // Don't forget to close the connection when you're done
                connection.close();
            } else {
                System.out.println("Failed to connect to the database!");
            }
        } catch (Exception e) {
            // Handle exceptions here
            e.printStackTrace();
        }
    }
}
