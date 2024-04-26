import React, { useState, useEffect } from 'react';
import axiosInstance from "../axios";
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';

const useStyles = makeStyles({
  root: {
    maxWidth: 300,
    margin: '1rem',
    textAlign: 'center',
  },
  media: {
    height: 200,
  },
  price: {
    marginTop: '1rem',
  },
});

function App() {
  
  useEffect(() => {
    fetchCurrentUser();
    console.log(name)
    
  });

  const [name, setUsername] = useState([]);

  const fetchCurrentUser = () => {
    axiosInstance.get('users/me/').then((res) => 
      setUsername(res.data['name'])).catch((error) => console.log(error));
    console.log(name)
  };

  const classes = useStyles();

  return (
    <div>
      <h2 style={{ textAlign: 'center' }}> Личный кабинет: </h2>
      <Grid container spacing={1}>(
          <Grid item xs={12} sm={6} md={4} key={name}>
            <Card className={classes.root}>
              <CardContent>
                <Typography variant="h5" component="h2">
                  Имя: {name}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
      </Grid>
    </div>
  );

}

export default App;