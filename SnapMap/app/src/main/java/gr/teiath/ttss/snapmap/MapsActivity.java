package gr.teiath.ttss.snapmap;

import android.content.Intent;
import android.net.Uri;
import android.os.Build;
import android.os.Environment;
import android.os.Handler;
import android.provider.MediaStore;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;
import android.support.v4.content.FileProvider;
import android.view.View;
import android.view.animation.AnimationUtils;
import android.widget.ImageButton;
import android.widget.Toast;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.CameraPosition;
import com.google.android.gms.maps.model.CircleOptions;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

import java.io.File;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback, GoogleMap.OnMarkerClickListener {

    private GoogleMap mMap;
    String imageName;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
        ImageButton cb = (ImageButton) findViewById(R.id.CameraButton);
        cb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                v.startAnimation(AnimationUtils.loadAnimation(MapsActivity.this, R.anim.image_click));
                (new Handler()).postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        takeImage();
                    }
                },600);
            }
        });
        ImageButton vb = (ImageButton) findViewById(R.id.ARButton);
        vb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                v.startAnimation(AnimationUtils.loadAnimation(MapsActivity.this, R.anim.image_click));
            }
        });
        ImageButton sb = (ImageButton) findViewById(R.id.SetButton);
        sb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                v.startAnimation(AnimationUtils.loadAnimation(MapsActivity.this, R.anim.image_click));
            }
        });
    }

    public void takeImage(){
        Intent imageIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        File imagesFolder = new File(Environment.getExternalStorageDirectory(), "SnapMap Images");
        imagesFolder.mkdirs();
        Integer unixTime = (int)(System.currentTimeMillis() / 1000L);
        imageName ="image_"+ unixTime.toString()+".jpg";
        File image = new File(imagesFolder, imageName);
        Uri uriSavedImage;
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.N) {
            uriSavedImage = Uri.fromFile(image);
        } else {
            uriSavedImage = FileProvider.getUriForFile(this,
                    BuildConfig.APPLICATION_ID + ".provider",
                    image);
        }
        imageIntent.putExtra(MediaStore.EXTRA_OUTPUT, uriSavedImage);
        startActivityForResult(imageIntent,1);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == 1) {
            if (resultCode == RESULT_OK) {
                // Image captured and saved to fileUri specified in the Intent
                Toast.makeText(this, "Image saved to \n" + imageName, Toast.LENGTH_LONG).show();
            } else if (resultCode == RESULT_CANCELED) {
                Toast.makeText(this, "Image capture cancelled", Toast.LENGTH_LONG).show();
            } else {
                // Image capture failed, advise user
            }
        }
    }


    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        mMap.setOnMarkerClickListener(this);

        LatLng teiath = new LatLng(38.003470, 23.675456);
        CameraPosition cameraPosition = new CameraPosition.Builder().target(teiath).tilt(90).zoom(17).bearing(0).build();
        mMap.animateCamera(CameraUpdateFactory.newCameraPosition(cameraPosition));
        mMap.addMarker(new MarkerOptions().position(teiath).title("TEI of Athens"));
        mMap.addCircle(new CircleOptions().center(teiath).radius(50).fillColor(0x100030A0).strokeColor(0x300030A0).strokeWidth(5));
    }

    @Override
    public boolean onMarkerClick(final Marker marker) {
        if(marker.getTitle().equals("TEI of Athens")){
            Toast.makeText(this, "TEI of Athens", Toast.LENGTH_SHORT).show();
        }
        return true;
    }
}
