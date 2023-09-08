package userApp;

public class addUserQury {

    addUserDTO dto = new addUserDTO();

    public String addUserData(){
        return "INSERT INTO users(id,name,father_name,contact,email) VALUES ("+dto.getId()+")";
    }
    
}
