const coworker = {
  from: coworkerData => {
    return {
      address: coworkerData.address,
      city: coworkerData.city,
      country: coworkerData.country,
      coworkerId: coworkerData.coworkerId,
      email: coworkerData.email,
      firstName: coworkerData.firstName,
      gender: coworkerData.gender,
      lastName: coworkerData.lastName,
      postalArea: coworkerData.postalArea,
      state: coworkerData.state,
      username: coworkerData.username
    };
  }
};

export default coworker;
