package studentManagmentSystem;
import java.util.Scanner;


public class studentAdd {

    private int id;
    private String firstName;
    private String lastName;
    private double cgpa;

    public studentAdd(int id, String firstName, String lastName, double cgpa) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.cgpa = cgpa;
    }

    // Getters and setters

    public int getId() {
        return id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public double getCgpa() {
        return cgpa;
    }

    public void setCgpa(double cgpa) {
        this.cgpa = cgpa;
    }

    @Override
    public String toString() {
        return "Student{" +
                "id=" + id +
                ", firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", cgpa=" + cgpa +
                '}';
    }

}
