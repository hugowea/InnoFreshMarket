import React, { useState, useEffect } from 'react';
import axiosInstance from "./axios";
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';

const useStyles = makeStyles({
  root: {
    maxWidth: 300,
    margin: '1rem',
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
    fetchProducts();
    console.log(products)
    
  }, []);

  const [products, setProducts] = useState([]);
  const [image, setImage] = useState('');

  const fetchProducts = () => {
    axiosInstance.get('users/items/').then((res) => 
      setProducts(res.data['items'])).catch((error) => { return (<div> <h2 style={{ textAlign: 'center' }}> Добро пожаловать! Войдите в аккаунт или зарегистрируйтесь </h2> </div>) });
  };

  const classes = useStyles();

  return (
    <div>
      <h2 style={{ textAlign: 'center' }}> Все доступные товары </h2>
      <Grid container spacing={3}>
        {products.map((product) => (
          <Grid item xs={12} sm={6} md={4} key={product.id}>
            <Card className={classes.root}>
              <CardMedia
                className={classes.CardMedia}
                image={product.doc}
                title={product.name}
              />
              <CardContent>
                <Typography variant="h5" component="h2">
                  {product.name}
                </Typography>
                <Typography className={classes.cost_retail} color="textSecondary">
                  Цена: {product.cost_retail} рублей
                </Typography>
                <Typography variant="body2" component="p">
                  {product.description}
                </Typography>
                <Typography variant="body2" component="p" color="textSecondary">
                  Количество доступных: {product.number}
                </Typography>
                <br></br>
                <Button variant="contained" color="green">
                  В корзину
                </Button>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </div>
  );

}

export default App;