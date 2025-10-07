import java.util.*;

public class BookingManager {


    List<Booking> bookingList = new ArrayList<>();


    public void registerBooking(Booking booking) {
        bookingList.add(booking);
    }


    public void showBookingsByDate(String date) {
        for (Booking b : bookingList) {
            if (b.bookingDate.equals(date)) {
                System.out.println(b);
            }
        }
    }
}