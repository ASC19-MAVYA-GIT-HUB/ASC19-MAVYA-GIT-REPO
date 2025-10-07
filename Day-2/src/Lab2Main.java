public class Lab2Main {
    public static void main(String[] args) {

        System.out.println(Lab2Utils.welcomeMessage("Mavya"));


        System.out.println("Maximum: " + Lab2Utils.largest(10, 25, 17));


        Lab2Utils.printDigitsInWords(951);


        BookingManager manager = new BookingManager();
        manager.registerBooking(new Booking("E101", "MR1", "2025-09-26", "10:00", 2));
        manager.registerBooking(new Booking("E102", "MR2", "2025-09-26", "14:00", 1));


        System.out.println("Bookings on 2025-09-26:");
        manager.showBookingsByDate("2025-09-26");
    }
}