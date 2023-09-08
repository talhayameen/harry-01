package userApp;

public class addUserQuery {

    addUserDTO dto = new addUserDTO();

    public String addUserData(){
        return "INSERT INTO users(id,name,father_name,contact,email) VALUES ("+dto.getId()+", '"+dto.getName()+"', '"+dto.getfatherName()+"', '"+dto.getContact()+"' , '"+dto.getEmail()+"')";
    }
    
}
