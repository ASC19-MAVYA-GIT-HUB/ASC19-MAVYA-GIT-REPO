public class SpecialMovie extends Movie {
    private String soundEffectsTechnology;
    private String visualEffectsTechnology;

    public SpecialMovie(String movieName, String producedBy, String directedBy, int duration, int year, String category,
                        String soundEffectsTechnology, String visualEffectsTechnology) {
        super(movieName, producedBy, directedBy, duration, year, category); // Call parent constructor
        this.soundEffectsTechnology = soundEffectsTechnology;
        this.visualEffectsTechnology = visualEffectsTechnology;
    }

    public String showSpecialDetails() {
        return super.showDetails() +
                "\nSound Effects: " + soundEffectsTechnology +
                "\nVisual Effects: " + visualEffectsTechnology;
    }
}
