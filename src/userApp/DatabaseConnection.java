package userApp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {

    private static Connection connection;

    public static Connection getConnection() {
        // if (connection == null) {
        //     try {
        //         String url = "jdbc:mysql://localhost:3307/userapp";
        //         String username = "root";
        //         String password = "password";
        //         connection = DriverManager.getConnection(url, username, password);
        //     } catch (SQLException e) {
        //         e.printStackTrace();
        //     }
        // }
        // return connection;

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            
        } catch (Exception e) {
            // TODO: handle exception
        }
    }
    
}
