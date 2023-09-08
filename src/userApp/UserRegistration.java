package userApp;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class UserRegistration {

    public static void registerUser(User user) {
        Connection connection = DatabaseConnection.getConnection();
        if (connection == null) {
            System.out.println("Failed to connect to the database.");
            return;
        }

        String sql = "INSERT INTO users (id, name, father_name, contact, email) VALUES (?, ?, ?, ?, ?)";

        try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setString(1, user.getName());
            preparedStatement.setString(2, user.getFatherName());
            preparedStatement.setString(3, user.getContact());
            preparedStatement.setString(4, user.getEmail());

            int rowsInserted = preparedStatement.executeUpdate();
            if (rowsInserted > 0) {
                System.out.println("User registered successfully!");
            } else {
                System.out.println("User registration failed.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        User user = new User();
        user.setName("John Doe");
        user.setFatherName("John's Father");
        user.setContact("1234567890");
        user.setEmail("john@example.com");

        registerUser(user);
    }
    
}
