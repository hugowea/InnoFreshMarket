import React, { useEffect } from 'react';
import axiosInstance from '../axios';
import { useNavigate } from 'react-router-dom';

export default function SignUp() {
	const history = useNavigate();

	useEffect(() => {
        
        console.log("Before: " + axiosInstance.defaults.headers['Authorization'] + " " + localStorage.getItem('access_token'))
		localStorage.removeItem('access_token');
		axiosInstance.defaults.headers['Authorization'] = null;
        
        console.log("After: " + axiosInstance.defaults.headers['Authorization'] + " " + localStorage.getItem('access_token'))
		history('/login');
	});
	return <div>Logout</div>;
}