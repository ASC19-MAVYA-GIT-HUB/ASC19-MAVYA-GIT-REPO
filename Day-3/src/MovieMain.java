public class MovieMain {
    public static void main(String[] args) {
        Movie m1 = new Movie("Hello", "XYZ Productions");
        System.out.println(m1.getMovieId()); // Output: Hello_1

        Movie m2 = new Movie("ActionBlast", "ABC Studios", "John Doe", 120, 2024, "Action");
        System.out.println(m2.showDetails());

        SpecialMovie sm = new SpecialMovie("EpicSound", "SoundWorks", "Jane Smith", 150, 2025, "Sci-Fi",
                "Dolby Atmos", "IMAX Enhanced");
        System.out.println(sm.showSpecialDetails());

        InternationalMovie im = new InternationalMovie("GlobalHit", "WorldWide Films", "Ali Khan", 110, 2023, "Drama",
                "France", "French");
        System.out.println(im.showInternationalDetails());

        System.out.println("Total Movies Created: " + Movie.getMoviesCount());
    }
}
