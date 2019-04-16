const coworker = {
  from: coworkerData => {
    return {
      address: coworkerData.address,
      city: coworkerData.city,
      country: coworkerData.country,
      coworkerId: coworkerData.coworker_id,
      email: coworkerData.email,
      firstName: coworkerData.firstName,
      gender: coworkerData.gender,
      lastName: coworkerData.lastName,
      postalArea: coworkerData.postal_area,
      state: coworkerData.state,
      username: coworkerData.username
    };
  }
};

export default coworker;
