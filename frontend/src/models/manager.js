const manager = {
  from: managerData => {
    return {
      address: managerData.address,
      city: managerData.city,
      country: managerData.country,
      coworkerId: managerData.coworker_id,
      email: managerData.email,
      firstName: managerData.firstName,
      gender: managerData.gender,
      lastName: managerData.lastName,
      postalArea: managerData.postal_area,
      state: managerData.state,
      username: managerData.username
    };
  }
};

export default manager;
