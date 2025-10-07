
public class LearnerApp {
    public static void main(String[] args) {
        LearnerArraysData app = new LearnerArraysData();
        app.assignLearnerNames();
        app.printLearnerNames();
        LearnerAnswersMap learnerAnswers = new LearnerAnswersMap();
        learnerAnswers.assignLearnerAnswers();
        learnerAnswers.displayLearnerAnswers();
    }
}
