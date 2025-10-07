public class Booking {


    String employeeId;
    String roomId;
    String bookingDate;
    String bookingTime;
    int durationHours;


    public Booking(String employeeId, String roomId, String bookingDate, String bookingTime, int durationHours) {
        this.employeeId = employeeId;
        this.roomId = roomId;
        this.bookingDate = bookingDate;
        this.bookingTime = bookingTime;
        this.durationHours = durationHours;
    }


    public String toString() {
        return "Booking: " + employeeId + " reserved " + roomId + " on " + bookingDate +
                " at " + bookingTime + " for " + durationHours + " hour(s).";
    }
}