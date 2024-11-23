#include <stdio.h> // 'stdio.h' contains declaration of printf()

// Entry-Point Function => main() => Valid Return Type (int) and 3 Parameters
//  (int argc, char *argv[], char *envp[])
int main(int argc, char *argv[], char *envp[])
{ 
    printf("\n\n");
    UserRegistration(formObject);

    return (0);
}


// Backend Flask API for user registration
void UserRegistration(string userObject)
{    
    printf("User Successfully Registered\n");
    // Create Python object from string
    // pass this instance to Database layer
    InserUser(userObj);

}


// Backend Implement Data Access Logic
void InserUser(User user)
{    
    printf("User Inserted in Database\n");
}
