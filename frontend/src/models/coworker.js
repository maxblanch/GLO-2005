const coworker = {
  from: coworkerData => {
    return {
      address: coworkerData.address,
      city: coworkerData.city,
      country: coworkerData.country,
      coworkerId: coworkerData.coworker_id,
      email: coworkerData.email,
      firstName: coworkerData.first_name,
      gender: coworkerData.gender,
      lastName: coworkerData.last_name,
      postalArea: coworkerData.postal_area,
      state: coworkerData.state,
      username: coworkerData.username
    };
  }
};

export default coworker;
