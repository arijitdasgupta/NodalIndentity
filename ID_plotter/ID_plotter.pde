//Visual rendition program
//Author: Arijit Dasgupta

int ht = 400;
int wd = 400;
int margin = 250;
int x_shift = margin;
int y_shift = margin;
int sq_wd = 150;
int N, depth;

int separationX, separationY;

String[] lines, params;
int counter = 0;

void setup(){
  lines = loadStrings("data.txt");
  params = loadStrings("params.txt");
  N = int(params[0]); //First line for square side
  depth = int(params[1]); //Second line for the max depth
  colorMode(HSB, depth, 1, 1, 100);
  size(wd, ht);
  rectMode(CENTER);
  noStroke();
  separationX = (wd - (2 * margin))/N;
  separationY = (ht - (2 * margin))/N;
}

void draw(){
  background(0,0,100, 100);
  if(counter < lines.length){
    //Write parsing code
    String[][] points = matchAll(lines[counter], "(([0-9]+,[0-9]+,[0-9]+))");
    for(int i = 0; i < points.length; i++){ //Parsing each point separately
      String[] vals = split(points[i][1], ',');
      int x = int(vals[0]);
      int y = int(vals[1]);
      int d = int(vals[2]);
      //Write drawing code
      fill(d, 1, 1, 75);
      rect(x * separationX + x_shift, y * separationY + y_shift, sq_wd/(d + 1), sq_wd/(d + 1), 4);
    }
    save("Images/image" + (counter + 1) + ".png");
  }
  else{
     noLoop();
     exit();
  }
  counter++;
}
