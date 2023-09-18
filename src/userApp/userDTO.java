package userApp;

public class userDTO {

    private int id;
    private String name;
    private String fatherName;
    private String contact;
    private String email;

    public int getId(){
       return id; 
    }
    public void setId(int id){
        this.id = id;
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getfatherName(){
        return fatherName;
    }

    }

    public String getContact(){
        return contact;
    }

    public void setContact(String contact){

        this.contact = contact;
    }

    public String getEmail(){
        return email;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public String result(){

        return "No Issue Found in DTO";
    }

    @Override
    public String toString(){
        return "UserDto [id=" + id + ", name=" + name + ", Father Name=" + fatherName + " , Contact="+contact+" , Email="+email+"]";
    }
}
