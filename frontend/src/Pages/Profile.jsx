import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Profile = () => {
  const [user, setUser] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    // Function to fetch user data from the server
    const fetchUserProfile = async () => {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          setError('No token found. Please log in.');
          return;
        }

        const userResponse = await axios.get('http://localhost:5555/protected', {
          headers: { 'Authorization': `Bearer ${token}` },
        });

        setUser(userResponse.data);
      } catch (err) {
        setError('Failed to fetch user data.');
      }
    };

    fetchUserProfile();
  }, []);

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white shadow-md rounded-md">
      <h1 className="text-2xl font-semibold text-gray-900">User Profile</h1>
      {error && <p className="text-red-500">{error}</p>}
      {user ? (
        <div className="mt-4">
          <div className="flex items-center">
            <div className="w-16 h-16 bg-gray-200 rounded-full overflow-hidden">
              {/* Placeholder for user avatar */}
              <img
                src="https://via.placeholder.com/64"
                alt="User avatar"
                className="w-full h-full object-cover"
              />
            </div>
            <div className="ml-4">
              <h2 className="text-xl font-medium text-gray-800">{user.username}</h2>
              <p className="text-gray-600">{user.email}</p>
            </div>
          </div>
          <div className="mt-4">
            <h3 className="text-lg font-medium text-gray-900">Bio</h3>
            <p className="text-gray-700">{user.bio || "No bio available."}</p>
          </div>
        </div>
      ) : (
        <p>Loading user data...</p>
      )}
    </div>
  );
};

export default Profile;
