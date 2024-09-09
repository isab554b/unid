<!-- IF USER DOES NOT HAVE SUBSCRIPTION -->
% if current_user and not current_user.get('has_active_subscription'):
<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_subscription"]["decorative_header_text"] }}
    </p>

    <h2>
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_subscription"]["header_text"] }}
    </h2>
  </div>
  <div class="">
    <!-- prettier-ignore -->
    % for subscription_key, subscription_value in services_and_prices_content['subscription_section']['subscriptions']['subscription_default'].items():
    <div>
      <div
        class="rounded-lg border-2 bg-unidYellow border-unidBlue flex flex-col"
      >
        <div class="flex flex-col lg:flex-row justify-between gap-6">
          <div class="text-unidDarkBlue space-y-1 p-6">
            <h3>{{ subscription_value["info"]["hours"] }}</h3>
          </div>
        </div>
        <div class="border-b border-unidLightBlue mx-6"></div>
        <div class="p-6 space-y-6">
          <div class="space-y-2">
            <!-- prettier-ignore -->
            % for point in subscription_value['selling_points']:
            <div class="flex items-center gap-2 text-unidDarkBlue">
              <div class="text-unidDarkBlue w-5 h-5">
                % include(global_content['ui_icons']['checkmark'])
              </div>
              <p>{{ point["text"] }}</p>
            </div>
            % end
          </div>
          <div class="flex items-center justify-between gap-4">
            <p class="text-unidDarkBlue text-base lg:text-lg">Pris</p>
            <div class="flex items-center gap-2">
              <p
                class="text-unidDarkBlue text-right text-2xl xl:text-3xl font-saira font-bold"
              >
                {{ subscription_value["info"]["price"] }}
              </p>
              <div class="flex flex-col text-xs text-unidDarkBlue">
                <p>ekskl.</p>
                <p>moms</p>
              </div>
            </div>
          </div>
          <!-- Display button -->
          <button
            type="button"
            id="primary_button"
            class="buy-button"
            data-subscription-type="{{ subscription_value['info']['hours'] }}"
            data-subscription-price="{{ subscription_value['info']['price'] }}"
            onclick="handleSubscriptionButtonClick(this)"
          >
            {{ subscription_value["button_text"] }}
          </button>
        </div>
      </div>
    </div>
    <!-- prettier-ignore -->
    % end
  </div>
</div>
<!-- IF USER HAS SUBSCRIPTION -->
% else:
<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_subscription"]["decorative_header_text"] }}
    </p>
    <h2>Dit abonnement</h2>
  </div>
  <div id="content_box_styling">
    <div id="content_box_header_styling">
      <div
        class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
      >
        <div id="icon_medium" class="fill-unidPurple">
          % include(global_content['ui_icons']['cart'])
        </div>
        <p class="font-bold text-lg text-white">Abonnement</p>
      </div>
    </div>
    <div class="flex flex-col gap-8 p-6 text-unidDarkBlue">
      <!-- USER -->
      <div class="space-y-2 text-sm">
        <div class="space-y-1">
          <p id="form_label">Dit abonnement indeholder:</p>
          <hr />
        </div>
        <div class="space-y-2">
          <div class="flex gap-2">
            <div class="text-unidDarkBlue w-5 h-5">
              % include(global_content['ui_icons']['checkmark'])
            </div>
            <p>Kontrol af ydeevne og hastighed for hjemmesiden</p>
          </div>
          <div class="flex gap-2">
            <div class="text-unidDarkBlue w-5 h-5">
              % include(global_content['ui_icons']['checkmark'])
            </div>
            <p>Opdatering af tema og plugins</p>
          </div>
          <div class="flex gap-2">
            <div class="text-unidDarkBlue w-5 h-5">
              % include(global_content['ui_icons']['checkmark'])
            </div>
            <p>Overvågning af website med Google Search Console</p>
          </div>
          <div class="flex gap-2">
            <div class="text-unidDarkBlue w-5 h-5">
              % include(global_content['ui_icons']['checkmark'])
            </div>
            <p>
              30 minutters sparring / vores ekspertise til udbedring af fejl
            </p>
          </div>
        </div>
      </div>
      <!-- prettier-ignore -->
      % if can_cancel:
      <div class="space-y-1">
        <p id="form_label">Opsig abonnement</p>
        <hr />
        <div class="space-y-1">
          <p class="text-unidDarkBlue text-sm">
            Ønsker du at opsige dit abonnement, bedes du udfylde nedenstående
            formular.
          </p>
          <p class="text-unidDarkBlue text-sm">
            Opsigelse af abonnementet skal ske inden månedens udgang. Hvis du
            opsiger midt i måneden, vil du ikke få refunderet betalingen for den
            resterende del af måneden.
          </p>
        </div>
      </div>
      <form
        id="cancelForm"
        action="/cancel-subscription"
        method="post"
        class="space-y-4"
      >
        <label for="full_name" class="space-y-1.5 block">
          <div class="flex space-between justify-between">
            <p id="form_label" class="text-sm">Navn</p>
          </div>
          <div class="relative w-full text-sm">
            <div
              class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidBlue rounded-bl-md rounded-tl-md"
            >
              <div id="icon_small" class="fill-white text-white w-5 h-5">
                % include(global_content['ui_icons']['user_circle'])
              </div>
            </div>
            <div
              class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidBlue rounded-bl-md rounded-tl-md"
            >
              <div id="icon_small" class="fill-white text-white w-5 h-5">
                % include(global_content['ui_icons']['user_circle'])
              </div>
            </div>
            <input
              id="form_input"
              type="text"
              name="full_name"
              placeholder="Lorem Ipsum"
              required
            />
          </div>
        </label>
        <label for="email" class="space-y-1.5 block">
          <div class="flex space-between justify-between">
            <p id="form_label" class="text-sm">Email</p>
          </div>
          <div class="relative w-full text-sm">
            <div
              class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidBlue rounded-bl-md rounded-tl-md"
            >
              <div id="icon_small" class="fill-white text-white w-5 h-5">
                % include(global_content['ui_icons']['email'])
              </div>
            </div>
            <div
              class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidBlue rounded-bl-md rounded-tl-md"
            >
              <div id="icon_small" class="fill-white text-white w-5 h-5">
                % include(global_content['ui_icons']['email'])
              </div>
            </div>
            <input
              id="form_input"
              type="email"
              name="email"
              placeholder="loremipsum@mail.dk"
              required
            />
          </div>
        </label>

        <label for="message" class="space-y-1.5 block">
          <div class="flex space-between justify-between">
            <p id="form_label" class="text-sm">Årsag til opsigelse</p>
          </div>
          <div class="relative w-full overflow-auto text-sm">
            <div
              class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidBlue h-full rounded-bl-md rounded-tl-md"
            >
              <div id="icon_small" class="fill-white text-white w-5 h-5">
                % include(global_content['ui_icons']['message'])
              </div>
            </div>
            <textarea
              id="form_input"
              class="-mb-1"
              type="message"
              name="message"
              inputmode="text"
              placeholder="Lorem ipsum dolor sit amet..."
              required
            ></textarea>
          </div>
        </label>

        <button type="submit" id="primary_button" class="cancel-submit-button">
          Opsig abonnement
        </button>
      </form>
      <p
        id="cancelMessageSent"
        style="display: none"
        class="text-unidDarkBlue text-sm"
      ></p>
      % else:
      <p class="text-unidDarkBlue text-sm">
        Du kan først opsige dit abonnement efter 3 måneder fra købsdatoen.
      </p>
      % end
    </div>
    % end
  </div>
</div>
% end
