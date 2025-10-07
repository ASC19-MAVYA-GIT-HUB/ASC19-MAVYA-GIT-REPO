import java.util.HashMap;
public class LearnerAnswersMap {
    HashMap<String,String> learnerAnswersMap = new HashMap<String,String>();
    public void assignLearnerAnswers() {
       learnerAnswersMap.put("Maheen", "Private variables cannot be accessed outside the class");
       learnerAnswersMap.put("Gagan", "The main method should always be main, otherwise we will not be able to run the program");
       learnerAnswersMap.put("Khyati", "The HashMap belongs to the java.util package");
       learnerAnswersMap.put("Mavya", "Identified the objects in a program");
       learnerAnswersMap.put("Anjali", "Identified the classes in the program");
       learnerAnswersMap.put("Khyati", "System defined classes : HashMap");
       learnerAnswersMap.put("Charisma","The String class ");
       learnerAnswersMap.put("Visranthi","Ordering :Unordered,Insertion Order,Sort Order");
       learnerAnswersMap.put("Awapna","Fetch the Key and value!");
       
    }
    //provided key and display the value.

    public void displayLearnerAnswers() {
        System.out.println("Maheen's answer: " + learnerAnswersMap.get("Maheen"));
        System.out.println("Gagan's answer: " + learnerAnswersMap.get("Gagan"));
        System.out.println("Khyati's answer: " + learnerAnswersMap.get("Khyati"));

    }
}
