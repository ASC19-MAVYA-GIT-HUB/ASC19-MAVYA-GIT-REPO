public class ZoomMeetingRoom extends MeetingRoom {


    String deviceId;
    String accountId;


    public ZoomMeetingRoom(String roomId, int capacity, int floorLevel, String deviceId, String accountId) {
        super(roomId, capacity, floorLevel);
        this.deviceId = deviceId;
        this.accountId = accountId;
    }
}