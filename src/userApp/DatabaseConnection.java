package userApp;

import java.sql.Connection;
import java.sql.DriverManager;

public class DatabaseConnection {

    //myMethod
    public void databaseConnection(){

        try {

            Class.forName("com.mysql.cj.jdbc.Driver");
            
            Connection connectionTest = DriverManager.getConnection("jdbc:mysql://localhost:3307/userapp?" + "user=root&password=password");

            if(connectionTest != null){

                System.out.println("Connected to the userApp");

                connectionTest.close();
            }
            else{
                System.out.println("Failed To connect userApp");
            }
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
