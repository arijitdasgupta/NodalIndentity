//Visual rendition program
//Author: Arijit Dasgupta

int ht = 400;
int wd = 400;
int margin = 250;
int x_shift = margin;
int y_shift = margin;
int sq_wd = 150;
int N, depth;
int out_square = 300;

int separationX, separationY;

String[] lines, params, names;
int counter = 0;

void setup(){
  lines = loadStrings("data.txt");
  params = loadStrings("params.txt");
  names = loadStrings("names.txt");
  N = int(params[0]); //First line for square side
  depth = int(params[1]); //Second line for the max depth
  colorMode(HSB, depth, 1, 1, 100);
  size(wd, ht);
  rectMode(CENTER);
  noStroke();
  separationX = (wd - (2 * margin))/N;
  separationY = (ht - (2 * margin))/N;
  smooth();
}

void draw(){
  background(0,0,100, 100);
  stroke(0,0,0,10);
  strokeWeight(20);
  noFill();
  rect(wd/2, ht/2, out_square, out_square, 10);
  if(counter < lines.length){
    //Write parsing code
    String[][] points = matchAll(lines[counter], "(([0-9]+,[0-9]+,[0-9]+))");
    for(int i = 0; i < points.length; i++){ //Parsing each point separately
      String[] vals = split(points[i][1], ',');
      int x = int(vals[0]);
      int y = int(vals[1]);
      int d = int(vals[2]);
      //Write drawing code
      noStroke();
      fill(d, 1, 1, 75);
      rect(x * separationX + x_shift, y * separationY + y_shift, sq_wd/(d + 1), sq_wd/(d + 1), 4);
    }
    save("Images/" + names[counter] + ".png");
  }
  else{
     noLoop();
     exit();
  }
  counter++;
}
