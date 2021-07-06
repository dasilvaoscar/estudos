package com.example.secondapp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        Log.i("OnCreate", "App está sendo criada")
    }

    override fun onStart() {
        super.onStart()
        Log.i("OnStart", "App startando")
    }

    override fun onResume() {
        super.onResume()
        Log.i("OnResume", "App armazenou estado da aplicação")
    }

    override fun onPause() {
        super.onPause()
        Log.i("OnPause", "App está sendo parado")
    }

    override fun onStop(){
        super.onStop()
        Log.i("onStop", "App parou")
    }

    override fun onRestart(){
        super.onRestart()
        Log.i("onRestart", "App restartou")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.i("onDestroy", "Remove da memória")
    }

    /*
    * Levando dados para outra activity
    * */
    private fun nextActivity(ActivityClass: AppCompatActivity) {
        val nextActivity = Intent(this, ActivityClass::class.java)
        startActivity(nextActivity)
    }

    fun onClickAqui(view: View) {
        /*
        * Seleção dos elementos por id
        **/
        val editInput = findViewById<EditText>(R.id.edt_name)
        val viewText = findViewById<TextView>(R.id.view_text)

        /*
        * Pega valor do input e altera na viewText
        * */
        val name: String = editInput.editableText.toString()
        viewText.text = name

        /*
        *  Chama a próxima activity
        * */
        this.nextActivity(NextActivity())
    }
}