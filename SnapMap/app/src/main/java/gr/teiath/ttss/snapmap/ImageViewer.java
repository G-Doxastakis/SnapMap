package gr.teiath.ttss.snapmap;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Window;
import android.webkit.WebView;

public class ImageViewer extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        getSupportActionBar().setTitle("Preview");
        setContentView(R.layout.activity_image_viewer);
        Intent i=getIntent();
        String url=i.getStringExtra("url");
        WebView webview=(WebView)findViewById(R.id.webview);
        webview.setInitialScale(30);
        webview.getSettings().setLoadWithOverviewMode(true);
        webview.getSettings().setUseWideViewPort(true);
        webview.loadUrl(url);
    }
    @Override
    public boolean onSupportNavigateUp(){
        finish();
        return true;
    }
}
